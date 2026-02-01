# Features.trimFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the Trim features within the component and supports the creation of new Trim features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<TrimFeatures> propertyValue = features_var->trimFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [TrimFeatures](TrimFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [trimFeatures.add](trimFeatures_add_Sample.htm) | Demonstrates the trimFeatures.add method. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |