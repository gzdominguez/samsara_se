Sub GenerateTempReport()
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''GenerateTempReport takes data from the Dashboard
''Sheet and converts is to Epoch format such that
''it can be passed into sens_hist.py as command args
''
''EpochStart = begin_time
''EpochStop = end_time
''EpochStop = increment_size
''''''''''''''''''''''''''''''''''''''''''''''''''''''

''variable assignments
Dim TimeStrt As Double
Dim TimeStop As Double
Dim TimeStep As String
Dim EpochStrt As Long
Dim EpochStop As Long
Dim EpochStep As Integer
Dim Ttype As String
''With statements enable for quicker compiling by disabling
''unneccessary functions
With Application
    .Calculation = xlCalculationManual
    .ScreenUpdating = False
    .DisplayAlerts = False
End With

''Values extracted from Dashboard Sheet
    TimeStrt = Worksheets("Dashboard").Cells(6, "M").Value
    TimeStop = Worksheets("Dashboard").Cells(7, "M").Value
    TimeStep = Worksheets("Dashboard").Cells(8, "M").Value

''Time Values converted from Excel Date to Epoch -- see Epoch function below
    EpochStrt = Epoch(TimeStrt)
    EpochStop = Epoch(TimeStop)

''Switch Case for setting step size
    Select Case TimeStep
        Case "milliseconds"
            EpochStep = 1
        Case "seconds"
            EpochStep = 1000
        Case "minutes"
            EpochStep = 60000
    End Select

''sens_hist.py call to query update table from csv
Shell (<full path of python.exe> " & "<full put of sens_hist.py> --b " & EpochStrt & " --i " & EpochStep & " --e " & EpochStop)
   
   
''wait function to allow for script to capture data (10 secs)
Application.Wait Now + #12:00:10 AM#

''refresh the power query of the csv file to ensure most recen
refresh

With Application
    .Calculation = xlCalculationAutomatic
    .DisplayAlerts = True
    .ScreenUpdating = True
End With

End Sub

Function Epoch(Time As Double)
'''''''''''''''''''''''''''''''''''''''''''''''''''''
''Function Converts Excel Date to Epoch Time
'''''''''''''''''''''''''''''''''''''''''''''''''''''
Epoch = (Time + (8 / 24) - 25569) * 86400
End Function

Sub refresh()
'''''''''''''''''''''''''''''''''''''''''''''''''''''
' Refresh temp_history sheet, then Dashboard sheet
'''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sheets("temp_history").Select
    Range("B20").Select
    Selection.ListObject.QueryTable.refresh BackgroundQuery:=False
    ActiveWorkbook.RefreshAll
    Sheets("Dashboard").Select
End Sub
