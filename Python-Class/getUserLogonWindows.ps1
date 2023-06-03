Get-EventLog -LogName Security -InstanceId 4624 | 
    ForEach-Object {
    #translate the raw data intoa new object
    [PSCustomObject]@{
        Time = $_.TimeGenerated
        User = "{0}\{1}" -f $_.ReplacementStrings[5], $_.ReplacementStrings[6]
        Type = $_.ReplacementStrings[10]
        "Source Network Address" = $_.ReplacementStrings[18]
        Target = $_.ReplacementStrings[19]
    }
}