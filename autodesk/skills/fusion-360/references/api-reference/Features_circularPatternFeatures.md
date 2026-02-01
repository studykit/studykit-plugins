# Features.circularPatternFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the circular pattern features within the component and supports the creation of new circular pattern features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<CircularPatternFeatures> propertyValue = features_var->circularPatternFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [CircularPatternFeatures](CircularPatternFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [circularPatternFeatures.add](circularPatternFeatures_add_Sample.htm) | Demonstrates the circularPatternFeatures.add method. To use the sample have a design open that contains at least one body. When you run the script, it will prompt you to select a body, which will be patterned around the base Y-axis. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |