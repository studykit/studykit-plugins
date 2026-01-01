# MultiAxisSingularitySettings.angle Property![](../images/TestTubeLarge.png)

Parent Object: [MultiAxisSingularitySettings](MultiAxisSingularitySettings.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MultiAxisSingularitySettings.h>

## Description

The minimum angular delta movement for the rotary axes before the singularity is adjusted. When fluctuations of the rotary axes are insignificant, this limit prevents adjustment of the tool axis vector. Typically set to 10 degrees or more. Value is in radians.

## Syntax

* [Python](#Python)
* [C++](#C++)

"multiAxisSingularitySettings\_var" is a variable referencing a MultiAxisSingularitySettings object. |

"multiAxisSingularitySettings\_var" is a variable referencing a MultiAxisSingularitySettings object. ```` ``` #include <Cam/Machine/MultiAxisSingularitySettings.h>  // Get the value of the property. double propertyValue = multiAxisSingularitySettings_var->angle();  // Set the value of the property, where value_var is a double. bool returnValue = multiAxisSingularitySettings_var->angle(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |