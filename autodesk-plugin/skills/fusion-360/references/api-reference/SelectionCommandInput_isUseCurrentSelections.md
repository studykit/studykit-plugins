# SelectionCommandInput.isUseCurrentSelections Property![](../images/TestTubeLarge.png)

Parent Object: [SelectionCommandInput](SelectionCommandInput.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SelectionCommandInput.h>

## Description

Determines if any selections the user has made before starting the command can be used by the command's selection inputs. The default is true, which means the active selections will be added to the first selection input whose selection filter allows for that entity type. For example, if you have two selection inputs that have filters to select any number of faces and there are four faces selected when the command is started, those four faces will be selected by the selection input. If there's another selection input for the same command that has the filter set to select sketch curves, and there are faces and sketch curves selected when you start the command, the faces will be selected by the selection input filtering for faces, and the sketch curves will be selected by the selection input filtering for sketch curves.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selectionCommandInput\_var" is a variable referencing a SelectionCommandInput object. |

"selectionCommandInput\_var" is a variable referencing a SelectionCommandInput object. ```` ``` #include <Core/UserInterface/SelectionCommandInput.h>  // Get the value of the property. boolean propertyValue = selectionCommandInput_var->isUseCurrentSelections();  // Set the value of the property, where value_var is a boolean. bool returnValue = selectionCommandInput_var->isUseCurrentSelections(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |