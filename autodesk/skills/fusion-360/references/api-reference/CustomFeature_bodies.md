# CustomFeature.bodies Property![](../images/TestTubeLarge.png)

Parent Object: [CustomFeature](CustomFeature.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CustomFeature.h>

## Description

Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customFeature\_var" is a variable referencing a CustomFeature object.  ```` ``` # Get the value of the property. propertyValue = customFeature_var.bodies ``` ```` |

"customFeature\_var" is a variable referencing a CustomFeature object. ```` ``` #include <Fusion/Features/CustomFeature.h>  // Get the value of the property. Ptr<BRepBodies> propertyValue = customFeature_var->bodies(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepBodies](BRepBodies.htm).

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |