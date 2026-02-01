# Features.moveFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the Move features within the component and supports the creation of new Move features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<MoveFeatures> propertyValue = features_var->moveFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [MoveFeatures](MoveFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [moveFeatures.add](moveFeatures_add_Sample.htm) | Demonstrates the moveFeatures.add method. |
| [Move Feature API Sample](MoveFeatureSample_Sample.htm) | Demonstrates creating a new move feature. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |