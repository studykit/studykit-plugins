# TabCommandInput.resourceFolder Property

Parent Object: [TabCommandInput](TabCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TabCommandInput.h>

## Description

Gets the folder that contains the icon for the tab. If no name is specified (no text on tab), a resourceFolder containing the icon needs to be provided. Icons can be defined using either PNG or SVG files. More information about icons can be found in the user manual topic [User Interface Customization](UserInterface_UM.htm#IconsForCommands).

## Syntax

* [Python](#Python)
* [C++](#C++)

"tabCommandInput\_var" is a variable referencing a TabCommandInput object. |

"tabCommandInput\_var" is a variable referencing a TabCommandInput object. ```` ``` #include <Core/UserInterface/TabCommandInput.h>  // Get the value of the property. string propertyValue = tabCommandInput_var->resourceFolder(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |