# Command.hasDistinctSelectionSets Property![](../images/TestTubeLarge.png)

Parent Object: [Command](Command.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

Determines if this selection input shares a common selection set with the other selection inputs of this command or its own unique selection set. The default is False, which means each selection input will have its own selection set. This means that the items in this selection set are only shown as selected when this selection input is active. As a result, other selection inputs associated with this command can select those same entities.

## Syntax

* [Python](#Python)
* [C++](#C++)

"command\_var" is a variable referencing a Command object. |

"command\_var" is a variable referencing a Command object. ```` ``` #include <Core/UserInterface/Command.h>  // Get the value of the property. boolean propertyValue = command_var->hasDistinctSelectionSets();  // Set the value of the property, where value_var is a boolean. bool returnValue = command_var->hasDistinctSelectionSets(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |