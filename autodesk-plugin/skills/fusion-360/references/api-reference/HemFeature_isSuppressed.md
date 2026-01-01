# HemFeature.isSuppressed Property![](../images/TestTubeLarge.png)

Parent Object: [HemFeature](HemFeature.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/HemFeature.h>

## Description

Gets and sets if this feature is suppressed. This is only valid for parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"hemFeature\_var" is a variable referencing a HemFeature object. |

"hemFeature\_var" is a variable referencing a HemFeature object. ```` ``` #include <Fusion/SheetMetal/HemFeature.h>  // Get the value of the property. boolean propertyValue = hemFeature_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = hemFeature_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |