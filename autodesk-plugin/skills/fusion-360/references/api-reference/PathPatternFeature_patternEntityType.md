# PathPatternFeature.patternEntityType Property

Parent Object: [PathPatternFeature](PathPatternFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PathPatternFeature.h>

## Description

Returns the type of entities the pattern consists of. This can be used to help determine the type of results that will be found in the pattern elements.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pathPatternFeature\_var" is a variable referencing a PathPatternFeature object. |

"pathPatternFeature\_var" is a variable referencing a PathPatternFeature object. ```` ``` #include <Fusion/Features/PathPatternFeature.h>  // Get the value of the property. PatternEntityTypes propertyValue = pathPatternFeature_var->patternEntityType(); ``` ```` |

## Property Value

This is a read only property whose value is a [PatternEntityTypes](PatternEntityTypes.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |