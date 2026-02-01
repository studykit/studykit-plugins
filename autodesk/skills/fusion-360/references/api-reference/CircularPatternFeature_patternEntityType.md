# CircularPatternFeature.patternEntityType Property

Parent Object: [CircularPatternFeature](CircularPatternFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CircularPatternFeature.h>

## Description

Returns the type of entities the pattern consists of. This can be used to help determine the type of results that will be found in the pattern elements.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circularPatternFeature\_var" is a variable referencing a CircularPatternFeature object. |

"circularPatternFeature\_var" is a variable referencing a CircularPatternFeature object. ```` ``` #include <Fusion/Features/CircularPatternFeature.h>  // Get the value of the property. PatternEntityTypes propertyValue = circularPatternFeature_var->patternEntityType(); ``` ```` |

## Property Value

This is a read only property whose value is a [PatternEntityTypes](PatternEntityTypes.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |