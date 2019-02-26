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
Dim TimeStrt As Date
Dim TimeStop As Date
Dim TDstrt As Double
Dim TDstop As Double
Dim TimeStep As String
Dim EpochStrt As Variant
Dim EpochStop As Variant
Dim EpochStep As Variant
Dim Path As String

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
    MsgBox TimeStrt
    
''Convert datatype from Date to Double
    TDstrt = CDbl(TimeStrt)
    TDstop = CDbl(TimeStop)
    
''Time Values converted from Excel Date to Epoch -- see Epoch function below
    EpochStrt = Epoch(TimeStrt)
    EpochStop = Epoch(TimeStop)

''Switch Case for setting step size
    Select Case TimeStep
        Case Is = "milliseconds"
            EpochStep = 1
        Case Is = "seconds"
            EpochStep = 1000
        Case Is = "minutes"
            EpochStep = 60000
    End Select
    
''sens_hist.py call to query update table from csv
''update the location of the python executable and the sens_hist.py script as necessary
    Path = "C:\Users\gd\AppData\Enthought\Canopy\User\python.exe C:\Users\gd\scripts\sens_hist.py --b " & EpochStrt & " --i " & EpochStep & " --e " & EpochStop
    RetVal = Shell (Path)

''wait function to allow for script to capture data (10 secs)
'' may need to increase this value for larger ranges and data point
'' to do this increase which ever time unit desired
'' #12:Minutes:Seconds
Application.Wait Now + #12:00:10 AM#

''refresh the power query of the csv file to ensure most recent
'''''''''''''''''''''''''''''''''''''''''''''''''''''
   ThisWorkbook.RefreshAll
Sheet("temp_history").Columns("D:D").NumberFormat = "m/d/yyyy h:mm"
   
With Application
    .Calculation = xlCalculationAutomatic
    .DisplayAlerts = True
    .ScreenUpdating = True
End With
End Sub


Function Epoch(Time As Variant)
'''''''''''''''''''''''''''''''''''''''''''''''''''''
''Function Converts Excel Date to Epoch Time
'''''''''''''''''''''''''''''''''''''''''''''''''''''
Epoch = (Time + (8 / 24) - 25569) * 86400
End Function
