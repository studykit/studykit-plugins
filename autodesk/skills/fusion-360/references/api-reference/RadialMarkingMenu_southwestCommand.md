# RadialMarkingMenu.southwestCommand Property

Parent Object: [RadialMarkingMenu](RadialMarkingMenu.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/RadialMarkingMenu.h>

## Description

Gets and sets the command definition that's displayed in the Southwest position (bottom-left) of the marking menu. Setting this to null indicates that the Southwest position should be empty.

## Syntax

* [Python](#Python)
* [C++](#C++)

"radialMarkingMenu\_var" is a variable referencing a RadialMarkingMenu object.  ```` ``` # Get the value of the property. propertyValue = radialMarkingMenu_var.southwestCommand  # Set the value of the property. radialMarkingMenu_var.southwestCommand = propertyValue ``` ```` |

"radialMarkingMenu\_var" is a variable referencing a RadialMarkingMenu object. ```` ``` #include <Core/UserInterface/RadialMarkingMenu.h>  // Get the value of the property. Ptr<Base> propertyValue = radialMarkingMenu_var->southwestCommand();  // Set the value of the property, where value_var is a Base. bool returnValue = radialMarkingMenu_var->southwestCommand(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Marking Menu API Sample](MarkingMenuSample_Sample.htm) | Demonstrates how to customize marking menu and context menu. This sample is an add-in. To use it, create a new add-in using the "Scrips and Add-Ins" command. Use any name you would like for the add-in. In the folder where the add-in was created edit the *add-in name*.py file and replace it's entire contents with the sample code below. You can also delete all the other files that were created for the add-in except for *add-in name*.manifiest. Start the add-in from the "Scripts and Add-Ins" dialog. Now, with the add-in running, whenever you right-click in the Fusion window, you'll get an entirely customized context menu. The default marking menu has been modified by the add-in by removing the existing commands and adding some custom commands. |

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |