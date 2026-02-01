# Palette.sendInfoToHTML Method

Parent Object: [Palette](Palette.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Palette.h>

## Description

Sends the string to the JavaScript associated with the loaded HTML.

## Remarks

A variation of the event handler below should be implemented in the JavaScript associated with the HTML to receive the data. The event will be triggered by Fusion whenever the sendInfoToHTML method is called.