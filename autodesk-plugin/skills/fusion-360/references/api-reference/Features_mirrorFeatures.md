# Features.mirrorFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the mirror features within the component and supports the creation of new mirror features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<MirrorFeatures> propertyValue = features_var->mirrorFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [MirrorFeatures](MirrorFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [mirrorFeatures.add](mirrorFeatures_add_Sample.htm) | Demonstrates the mirrorFeatures.add method by mirroring the selected body around the base X-Y construction plane. |
| [Mirror Feature API Sample](MirrorFeatureSample_Sample.htm) | Demonstrates creating a new mirror feature |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |