function Send-CPAPIRequest {
[CmdletBinding(DefaultParameterSetName="NoAuth")]

    param (
        [Parameter(Position=1,Mandatory=$true,ValueFromPipeline=$true,ValueFromPipelineByPropertyName=$true)]
        [Alias("Cn","MachineName","PSComputerName","SystemName")]
        [string[]]
        $ComputerName,

        [Parameter(Position=2,Mandatory=$true)]
        [string]
        $URI,

        [Parameter(Position=3,Mandatory=$false)]
        [ValidateSet("GET","POST","HEAD","DELETE","OPTIONS","PUT","PATCH")]
        [string]
        $Method = 'GET',

        [Parameter(Mandatory=$false)]
        [string]
        $Protocol = 'http',

        [Parameter(Mandatory=$false)]
        [string]
        $UserAgent = 'Powershell/Send-CPAPIRequest/1.0',

        [Parameter(Mandatory=$false)]
        [string]
        $HostHeader = '',

        [Parameter(Mandatory=$false)]
        [switch]
        $UpgradeRequiredPassThrough,
        [Parameter(Mandatory=$false,ParameterSetName="NoAuth")] # Param is defined this way to create the default ParamSet
        [Parameter(Mandatory=$false,ParameterSetName="BasicAuth")]
        [Parameter(Mandatory=$false,ParameterSetName="TokenAuth")]
        [hashtable]
        $Headers = @{},

        [Parameter(Position=4,Mandatory=$true,ParameterSetName="BasicAuth")]
        [string]
        $Login,

        [Parameter(Position=5,Mandatory=$true,ParameterSetName="BasicAuth")]
        [string]
        $Password,

        [Parameter(Position=4,Mandatory=$true,ParameterSetName="TokenAuth")]
        [Alias("Token")]
        [string]
        $AuthorizationToken
    )

    begin {
        [hashtable]$ReqHeaders = @{}

        #if it needs authorization
        if ($Login) {
            $Base64Auth = [System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes("$login`:$password"))
            $ReqHeaders.Add('Authorization',"Basic $Base64Auth")
        }
        elseif ($AuthorizationToken) {
            $ReqHeaders.Add('Authorization',"Token token=`"$AuthorizationToken`"")
        }

        if ($HostHeader -ne '') {
            $ReqHeaders["Host"] = $HostHeader
        }

        foreach($header in $Headers.Keys) {
            $ReqHeaders[$header] = $Headers[$header]
        }

        $result = $null

        if ($URI -notmatch "^\/") {$URI = "/$URI"}
    }

    process {
        foreach ($Comp in $ComputerName) {
            do {
                try {
                
                    Write-Verbose "Requesting $Comp with headers:"
                    if ($ReqHeaders.Keys) {
                        $ReqHeaders.Keys | % { Write-Verbose "`t$_`: $($ReqHeaders[$_])"}
                    }
                    else {
                        Write-Verbose "[No headers]"
                    }

                    $result = Invoke-WebRequest -UseBasicParsing -Uri "$Protocol`://$Comp$URI" -Headers $ReqHeaders -Method $Method -ErrorAction SilentlyContinue -UserAgent $user_agent 

                }
                catch [System.Net.WebException] {
                    $result = $_.Exception.Response
    
                }

                if (!$UpgradeRequiredPassThrough -and $result.StatusCode -eq "UpgradeRequired" -and $ReqHeaders["x-original-protocol"] -ne "https") {
                    $ReqHeaders["x-original-protocol"] = "https"
                    Write-Verbose ""
                    Write-Verbose "UpgradeRequired status received. Retrying with x-original-protocol:https header"
                }
                else {
                    break;
                }

            } while ($true)
            #finally {
                Write-Verbose "Status : $($result.StatusCode)"

                $result
                $result = $null
            #}
        }
    }
}

New-Alias api Send-CPAPIRequest -ErrorAction SilentlyContinue