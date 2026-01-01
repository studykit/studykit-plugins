# Features.untrimFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the Untrim features within the component and supports the creation of new Untrim features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<UntrimFeatures> propertyValue = features_var->untrimFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [UntrimFeatures](UntrimFeatures.htm).

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |