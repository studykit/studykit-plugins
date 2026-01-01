# StitchFeature.name Property

Parent Object: [StitchFeature](StitchFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/StitchFeature.h>

## Description

Returns the name of the feature as seen in the browser (non-parametric) or in the timeline (parametric).

## Syntax

* [Python](#Python)
* [C++](#C++)

"stitchFeature\_var" is a variable referencing a StitchFeature object. |

"stitchFeature\_var" is a variable referencing a StitchFeature object. ```` ``` #include <Fusion/Features/StitchFeature.h>  // Get the value of the property. string propertyValue = stitchFeature_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = stitchFeature_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |