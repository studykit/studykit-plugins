# BrowserCommandInput.sendInfoToHTML Method

Parent Object: [BrowserCommandInput](BrowserCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/BrowserCommandInput.h>

## Description

Sends a string to the JavaScript associated with the loaded HTML.

## Remarks

A variation of the event handler below should be implemented in the JavaScript associated with the HTML to receive the data. The event will be triggered by Fusion whenever the sendInfoToHTML method is called.