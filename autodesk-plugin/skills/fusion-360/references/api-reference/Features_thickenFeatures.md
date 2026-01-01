# Features.thickenFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the Thicken features within the component and supports the creation of new Thicken features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<ThickenFeatures> propertyValue = features_var->thickenFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [ThickenFeatures](ThickenFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [thickenFeatures.add](thickenFeatures_add_Sample.htm) | Demonstrates the thickenFeatures.add method. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |