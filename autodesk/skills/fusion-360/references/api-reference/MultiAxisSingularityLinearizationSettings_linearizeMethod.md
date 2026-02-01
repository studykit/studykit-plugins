# MultiAxisSingularityLinearizationSettings.linearizeMethod Property![](../images/TestTubeLarge.png)

Parent Object: [MultiAxisSingularityLinearizationSettings](MultiAxisSingularityLinearizationSettings.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MultiAxisSingularityLinearizationSettings.h>

## Description

The linearization method to use for the multi-axis singularity settings.

## Syntax

* [Python](#Python)
* [C++](#C++)

"multiAxisSingularityLinearizationSettings\_var" is a variable referencing a MultiAxisSingularityLinearizationSettings object. |

"multiAxisSingularityLinearizationSettings\_var" is a variable referencing a MultiAxisSingularityLinearizationSettings object. ```` ``` #include <Cam/Machine/MultiAxisSingularityLinearizationSettings.h>  // Get the value of the property. MultiAxisSingularityLinearizeMethod propertyValue = multiAxisSingularityLinearizationSettings_var->linearizeMethod();  // Set the value of the property, where value_var is a MultiAxisSingularityLinearizeMethod. bool returnValue = multiAxisSingularityLinearizationSettings_var->linearizeMethod(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [MultiAxisSingularityLinearizeMethod](MultiAxisSingularityLinearizeMethod.htm).

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |