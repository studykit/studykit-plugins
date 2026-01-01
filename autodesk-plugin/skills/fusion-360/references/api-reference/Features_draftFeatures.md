# Features.draftFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the draft features within the component and supports the creation of new draft features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<DraftFeatures> propertyValue = features_var->draftFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [DraftFeatures](DraftFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [draftFeatures.add](draftFeatures_add_Sample.htm) | Demonstrates the draftFeatures.add method. To use this sample, have a design open that contains at least one body. When you run the sample, you will be prompted to select the face to draft. Because the pull direction is using the base X-Y plane, you need to select a face that is not parallel to the X-Y plane. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |