# Features.filletFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the fillet features within the component and supports the creation of new fillet features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<FilletFeatures> propertyValue = features_var->filletFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [FilletFeatures](FilletFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [filletFeatures.add](filletFeatures_add_Sample.htm) | Demonstrates the filletFeatures.add method. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |