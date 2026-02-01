# Curve3DPath.count Property![](../images/TestTubeLarge.png)

Parent Object: [Curve3DPath](Curve3DPath.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::core" and the header file is <Core/Geometry/Curve3DPath.h>

## Description

Returns the number of Curve3D objects contained in this Curve3D collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curve3DPath\_var" is a variable referencing a Curve3DPath object. |

"curve3DPath\_var" is a variable referencing a Curve3DPath object. ```` ``` #include <Core/Geometry/Curve3DPath.h>  // Get the value of the property. uinteger propertyValue = curve3DPath_var->count(); ``` ```` |

## Property Value

This is a read only property whose value is a uinteger.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |