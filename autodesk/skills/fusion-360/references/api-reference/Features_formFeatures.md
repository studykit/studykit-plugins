# Features.formFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the existing form features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<FormFeatures> propertyValue = features_var->formFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [FormFeatures](FormFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [formFeatures.add](formFeatures_add_Sample.htm) | Demonstrates the formFeatures.add method. This creates a new empty form (T-Spline) feature, which you'll see in the timeline. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |