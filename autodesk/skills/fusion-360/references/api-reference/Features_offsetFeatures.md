# Features.offsetFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the Offset features within the component and supports the creation of new Offset features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<OffsetFeatures> propertyValue = features_var->offsetFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is an [OffsetFeatures](OffsetFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [offsetFeatures.add](offsetFeatures_add_Sample.htm) | Demonstrates the offsetFeatures.add method. This is the equivalent of the Offset command in the SURFACE tab. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |