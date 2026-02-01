# PatternElement.occurrences Property

Parent Object: [PatternElement](PatternElement.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatternElement.h>

## Description

If the patternEntityType property of the parent feature returns OccurrencesPatternType then this property will return the occurrences associated with this particular pattern element.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patternElement\_var" is a variable referencing a PatternElement object. |

"patternElement\_var" is a variable referencing a PatternElement object. ```` ``` #include <Fusion/Features/PatternElement.h>  // Get the value of the property. std::vector<Ptr<Occurrence>> propertyValue = patternElement_var->occurrences(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [Occurrence](Occurrence.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |