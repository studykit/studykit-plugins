# BoolValueCommandInput.resourceFolder Property

Parent Object: [BoolValueCommandInput](BoolValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/BoolValueCommandInput.h>

## Description

Gets and sets the folder that contains the icon to display on the button. Text can also be displayed, which is specified using the text property. More information about icons can be found in the user manual topic [User Interface Customization](UserInterface_UM.htm#IconsForCommands).

## Syntax

* [Python](#Python)
* [C++](#C++)

"boolValueCommandInput\_var" is a variable referencing a BoolValueCommandInput object. |

"boolValueCommandInput\_var" is a variable referencing a BoolValueCommandInput object. ```` ``` #include <Core/UserInterface/BoolValueCommandInput.h>  // Get the value of the property. string propertyValue = boolValueCommandInput_var->resourceFolder();  // Set the value of the property, where value_var is a string. bool returnValue = boolValueCommandInput_var->resourceFolder(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |