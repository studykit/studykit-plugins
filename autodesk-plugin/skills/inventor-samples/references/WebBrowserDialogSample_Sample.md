# WebBrowserDialog creation

## Description

This sample demonstrates how to create a web-based browser dialog, you can use this dialog to show a html format file or navigate to a website etc..

## Code Samples

* [VBA](#VBA)

```
Sub WebBrowserDialogSample()
    ' Create a WebBrowserDialog
    Dim oWebBrowserDialog As WebBrowserDialog
    Set oWebBrowserDialog = ThisApplication.WebBrowserDialogs.Add("MyBrowser")
    oWebBrowserDialog.WindowState = kNormalWindow

    ' Nagigate to a web site
    Call oWebBrowserDialog.Navigate("http://www.autodesk.com")

    ' Play a tutorial video if you have the Interactive Tutorial installed
    ' Call oWebBrowserDialog.Navigate("C:\Users\Public\Documents\Autodesk\Inventor 2017\Interactive Tutorial\en-US\Fundamentals\Video\Drawings.webm")

    ' Delete it
    oWebBrowserDialog.Delete
End Sub
```
