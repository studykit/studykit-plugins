# Features.mergeFacesFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection object that supports the ability to merge faces. Merging faces is currently limited to a Direct Modeling design or a body in a base feature. The result of merging faces is a direct B-Rep modification, and the change is not represented as a feature in the browser.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<MergeFacesFeatures> propertyValue = features_var->mergeFacesFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [MergeFacesFeatures](MergeFacesFeatures.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |