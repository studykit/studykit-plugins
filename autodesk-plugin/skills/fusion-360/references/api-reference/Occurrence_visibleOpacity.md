# Occurrence.visibleOpacity Property

Parent Object: [Occurrence](Occurrence.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrence.h>

## Description

The user can set an override opacity for components and these opacity overrides combine if children and parent components have overrides. This property returns the actual opacity that is being used to render the occurrence. To set the opacity use the opacity property of the Component object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrence\_var" is a variable referencing an Occurrence object. |

"occurrence\_var" is a variable referencing an Occurrence object. ```` ``` #include <Fusion/Components/Occurrence.h>  // Get the value of the property. double propertyValue = occurrence_var->visibleOpacity(); ``` ```` |

## Property Value

This is a read only property whose value is a double.

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |