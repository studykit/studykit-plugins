# LinearMarkingMenu.controls Property

Parent Object: [LinearMarkingMenu](LinearMarkingMenu.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/LinearMarkingMenu.h>

## Description

Return the collection of top-level controls in the context menu. It's possible to have drop-down controls (fly-outs) that provide access to additional controls. You can remove and add controls to customize the contents of the context menu.

## Syntax

* [Python](#Python)
* [C++](#C++)

"linearMarkingMenu\_var" is a variable referencing a LinearMarkingMenu object. |

"linearMarkingMenu\_var" is a variable referencing a LinearMarkingMenu object. ```` ``` #include <Core/UserInterface/LinearMarkingMenu.h>  // Get the value of the property. Ptr<ToolbarControls> propertyValue = linearMarkingMenu_var->controls(); ``` ```` |

## Property Value

This is a read only property whose value is a [ToolbarControls](ToolbarControls.htm).

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