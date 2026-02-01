# FusionProductPreferences.isAutoLookAtSketch2 Property

Parent Object: [FusionProductPreferences](FusionProductPreferences.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionProductPreferences.h>

## Description

Gets and sets if the view is re-oriented to view the newly created sketch, and if it is re-oriented, if the camera uses the current camera settings or is orthographic.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionProductPreferences\_var" is a variable referencing a FusionProductPreferences object. |

"fusionProductPreferences\_var" is a variable referencing a FusionProductPreferences object. ```` ``` #include <Fusion/Fusion/FusionProductPreferences.h>  // Get the value of the property. AutoLookAtSketchSettings propertyValue = fusionProductPreferences_var->isAutoLookAtSketch2();  // Set the value of the property, where value_var is an AutoLookAtSketchSettings. bool returnValue = fusionProductPreferences_var->isAutoLookAtSketch2(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [AutoLookAtSketchSettings](AutoLookAtSketchSettings.htm).

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |