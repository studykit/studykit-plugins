# MultiAxisRetractAndReconfigureSettings.stockExpansion Property![](../images/TestTubeLarge.png)

Parent Object: [MultiAxisRetractAndReconfigureSettings](MultiAxisRetractAndReconfigureSettings.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MultiAxisRetractAndReconfigureSettings.h>

## Description

Defines the stock expansion for computing retract moves in rewinds.

## Syntax

* [Python](#Python)
* [C++](#C++)

"multiAxisRetractAndReconfigureSettings\_var" is a variable referencing a MultiAxisRetractAndReconfigureSettings object. |

"multiAxisRetractAndReconfigureSettings\_var" is a variable referencing a MultiAxisRetractAndReconfigureSettings object. ```` ``` #include <Cam/Machine/MultiAxisRetractAndReconfigureSettings.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = multiAxisRetractAndReconfigureSettings_var->stockExpansion();  // Set the value of the property, where value_var is a Vector3D. bool returnValue = multiAxisRetractAndReconfigureSettings_var->stockExpansion(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |