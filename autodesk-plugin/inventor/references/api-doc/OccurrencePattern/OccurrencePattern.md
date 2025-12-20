# OccurrencePattern Object

## Description

The OccurrencePattern object is the base class for the FeatureBasedOccurrencePattern, RectangularOccurrencePattern, and CircularOccurrencePattern objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../OccurrencePattern/OccurrencePattern_Delete.md) | Method that deletes the pattern. |
| [GetReferenceKey](../OccurrencePattern/OccurrencePattern_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [Suppress](../OccurrencePattern/OccurrencePattern_Suppress.md) | Suppress the occurrence pattern. |
| [Unsuppress](../OccurrencePattern/OccurrencePattern_Unsuppress.md) | Unsuppress the occurrence pattern. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../OccurrencePattern/OccurrencePattern_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../OccurrencePattern/OccurrencePattern_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [HealthStatus](../OccurrencePattern/OccurrencePattern_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsPatternElement](../OccurrencePattern/OccurrencePattern_IsPatternElement.md) | Property that indicates whether this occurrence pattern is itself an element of a parent pattern. In the case where this occurrence pattern represents a pattern element, this property returns True. The PatternElement property can be used to get that pattern element. |
| [Name](../OccurrencePattern/OccurrencePattern_Name.md) | Gets/Sets the name for the pattern. |
| [OccurrencePatternElements](../OccurrencePattern/OccurrencePattern_OccurrencePatternElements.md) | Property returning an OccurrencePatternElements collection object. The first element within this collection will contain the components that were provided as input for the pattern. |
| [Parent](../OccurrencePattern/OccurrencePattern_Parent.md) | Property that returns the parent of the object. |
| [ParentComponents](../OccurrencePattern/OccurrencePattern_ParentComponents.md) | Property that gets and sets the components used as input for the pattern. |
| [PatternElement](../OccurrencePattern/OccurrencePattern_PatternElement.md) | Property that returns the pattern element this occurrence pattern represents. In the case where this occurrence pattern is not part of a parent pattern this property returns Nothing. The IsPatternElement property can be used to check if this occurrence pattern is part of a parent pattern. |
| [Suppressed](../OccurrencePattern/OccurrencePattern_Suppressed.md) | Returns the suppress state of the occurrence pattern. |
| [Type](../OccurrencePattern/OccurrencePattern_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../OccurrencePattern/OccurrencePattern_Visible.md) | Gets/Sets the Visible property for the pattern. |

## Accessed From

[OccurrencePatternElements.Parent](../OccurrencePatternElements/OccurrencePatternElements_Parent.md), [OccurrencePatterns.Item](../OccurrencePatterns/OccurrencePatterns_Item.md)

## Derived Classes

[CircularOccurrencePattern](../CircularOccurrencePattern/CircularOccurrencePattern.md), [FeatureBasedOccurrencePattern](../FeatureBasedOccurrencePattern/FeatureBasedOccurrencePattern.md), [RectangularOccurrencePattern](../RectangularOccurrencePattern/RectangularOccurrencePattern.md)

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |