# Features.removeFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the Remove features within the component and supports the creation of new Remove features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<RemoveFeatures> propertyValue = features_var->removeFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [RemoveFeatures](RemoveFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [removeFeatures.add](removeFeatures_add_Sample.htm) | Demonstrate the removeFeatures.add method. The Remove feature is the same as selecting a body in the browser and selecting "Remove" in the context menu. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |