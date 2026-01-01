# RectangularPatternFeature.patternElements Property

Parent Object: [RectangularPatternFeature](RectangularPatternFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RectangularPatternFeature.h>

## Description

Gets the PatternElements collection that contains the elements created by this pattern.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternFeature\_var" is a variable referencing a RectangularPatternFeature object. |

"rectangularPatternFeature\_var" is a variable referencing a RectangularPatternFeature object. ```` ``` #include <Fusion/Features/RectangularPatternFeature.h>  // Get the value of the property. Ptr<PatternElements> propertyValue = rectangularPatternFeature_var->patternElements(); ``` ```` |

## Property Value

This is a read only property whose value is a [PatternElements](PatternElements.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |