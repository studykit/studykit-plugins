# Occurrence.breakLink Method

Parent Object: [Occurrence](Occurrence.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrence.h>

## Description

When the component this occurrence references is an external reference (the isReferencedComponent property returns true), this will break the link and create a local Component that this occurrence will reference. The new local Component can be accessed through the Occurrence using the component property.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrence\_var" is a variable referencing an [Occurrence](Occurrence.htm) object.```` ``` returnValue = occurrence_var.breakLink() ``` ```` |

"occurrence\_var" is a variable referencing an [Occurrence](Occurrence.htm) object.  ```` ``` #include <Fusion/Components/Occurrence.h>  returnValue = occurrence_var->breakLink(); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the break link was successful. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Break Link API Sample](BreakLink_Sample.htm) | Iterates over all top-level occurrences and if it's a referenced component, it will break the link. |

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |