# Features.revolveFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the revolve features within the component and supports the creation of new revolved features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<RevolveFeatures> propertyValue = features_var->revolveFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [RevolveFeatures](RevolveFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [revolveFeatures.add](revolveFeatures_add_Sample.htm) | Demonstrates creating a revolve feature using an angle extent. |
| [Simple Revolve Feature Sample](SimpleRevolveFeatureSample_Sample.htm) | Creates a new revolve feature, resulting in a new component. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |