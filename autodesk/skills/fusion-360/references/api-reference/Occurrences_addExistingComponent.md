# Occurrences.addExistingComponent Method

Parent Object: [Occurrences](Occurrences.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrences.h>

## Description

Method that creates a new occurrence using an existing component. This is the equivalent of copying and pasting an occurrence in the user interface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrences\_var" is a variable referencing an [Occurrences](Occurrences.htm) object.```` ``` returnValue = occurrences_var.addExistingComponent(component, transform) ``` ```` |

"occurrences\_var" is a variable referencing an [Occurrences](Occurrences.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Occurrence](Occurrence.htm) | Returns the newly created occurrence or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| component | [Component](Component.htm) | The existing component to create a new occurrence of. |
| transform | [Matrix3D](Matrix3D.htm) | A transform that defines the location for the new occurrence |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Component Sample](ComponentSample_Sample.htm) | Component related functions |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |