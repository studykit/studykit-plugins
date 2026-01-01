# FilletFeature.filletFeatureType Property

Parent Object: [FilletFeature](FilletFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletFeature.h>

## Description

Returns the FilletFeatureTypes indicating this fillet feature type.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filletFeature\_var" is a variable referencing a FilletFeature object. |

"filletFeature\_var" is a variable referencing a FilletFeature object. ```` ``` #include <Fusion/Features/FilletFeature.h>  // Get the value of the property. FilletFeatureTypes propertyValue = filletFeature_var->filletFeatureType(); ``` ```` |

## Property Value

This is a read only property whose value is a [FilletFeatureTypes](FilletFeatureTypes.htm).

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |