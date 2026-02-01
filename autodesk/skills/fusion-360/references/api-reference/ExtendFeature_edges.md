# ExtendFeature.edges Property

Parent Object: [ExtendFeature](ExtendFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtendFeature.h>

## Description

Gets the edges that were extended. In many cases the extend operation results in the edges being consumed so they're no longer available after the feature is created. in this case you need to reposition the timeline marker to just before this feature when the edges do exist.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extendFeature\_var" is a variable referencing an ExtendFeature object.  ```` ``` # Get the value of the property. propertyValue = extendFeature_var.edges ``` ```` |

"extendFeature\_var" is a variable referencing an ExtendFeature object. ```` ``` #include <Fusion/Features/ExtendFeature.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = extendFeature_var->edges(); ``` ```` |

## Property Value

This is a read only property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |