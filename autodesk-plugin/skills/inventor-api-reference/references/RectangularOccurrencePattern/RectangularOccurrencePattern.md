# RectangularOccurrencePattern Object

Derived from: [OccurrencePattern](../OccurrencePattern/OccurrencePattern.md) Object

## Description

The RectangularOccurrencePattern object represents a rectangular pattern of assembly occurrences.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../RectangularOccurrencePattern/RectangularOccurrencePattern_Delete.md) | Method that deletes the pattern. |
| [GetReferenceKey](../RectangularOccurrencePattern/RectangularOccurrencePattern_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [Suppress](../RectangularOccurrencePattern/RectangularOccurrencePattern_Suppress.md) | Suppress the occurrence pattern. |
| [Unsuppress](../RectangularOccurrencePattern/RectangularOccurrencePattern_Unsuppress.md) | Unsuppress the occurrence pattern. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../RectangularOccurrencePattern/RectangularOccurrencePattern_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../RectangularOccurrencePattern/RectangularOccurrencePattern_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ColumnCount](../RectangularOccurrencePattern/RectangularOccurrencePattern_ColumnCount.md) | Property returning the Parameter object that controls the number of columns. |
| [ColumnEntity](../RectangularOccurrencePattern/RectangularOccurrencePattern_ColumnEntity.md) | Gets/Sets the entity used to define the column (x) direction of the pattern. |
| [ColumnEntityNaturalDirection](../RectangularOccurrencePattern/RectangularOccurrencePattern_ColumnEntityNaturalDirection.md) | Gets/Sets whether the column direction is in the natural direction of the column entity or not. |
| [ColumnOffset](../RectangularOccurrencePattern/RectangularOccurrencePattern_ColumnOffset.md) | Property returning the Parameter object that controls the distance between columns. |
| [HealthStatus](../RectangularOccurrencePattern/RectangularOccurrencePattern_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsPatternElement](../RectangularOccurrencePattern/RectangularOccurrencePattern_IsPatternElement.md) | Property that indicates whether this occurrence pattern is itself an element of a parent pattern. In the case where this occurrence pattern represents a pattern element, this property returns True. The PatternElement property can be used to get that pattern element. |
| [Name](../RectangularOccurrencePattern/RectangularOccurrencePattern_Name.md) | Gets/Sets the name for the pattern. |
| [OccurrencePatternElement](../RectangularOccurrencePattern/RectangularOccurrencePattern_OccurrencePatternElement.md) | Property returning a specific element within a pattern. The pattern element returned for row 1, column 1 will contain the components that were provided as input for the pattern. |
| [OccurrencePatternElements](../RectangularOccurrencePattern/RectangularOccurrencePattern_OccurrencePatternElements.md) | Property returning an OccurrencePatternElements collection object. The first element within this collection will contain the components that were provided as input for the pattern. |
| [Parent](../RectangularOccurrencePattern/RectangularOccurrencePattern_Parent.md) | Property that returns the parent of the object. |
| [ParentComponents](../RectangularOccurrencePattern/RectangularOccurrencePattern_ParentComponents.md) | Property that gets and sets the components used as input for the pattern. |
| [PatternElement](../RectangularOccurrencePattern/RectangularOccurrencePattern_PatternElement.md) | Property that returns the pattern element this occurrence pattern represents. In the case where this occurrence pattern is not part of a parent pattern this property returns Nothing. The IsPatternElement property can be used to check if this occurrence pattern is part of a parent pattern. |
| [RowCount](../RectangularOccurrencePattern/RectangularOccurrencePattern_RowCount.md) | Property returning the Parameter object that controls the number of rows. |
| [RowEntity](../RectangularOccurrencePattern/RectangularOccurrencePattern_RowEntity.md) | Gets/Sets the entity used to define the row (x) direction of the pattern. |
| [RowEntityNaturalDirection](../RectangularOccurrencePattern/RectangularOccurrencePattern_RowEntityNaturalDirection.md) | Gets/Sets whether the row direction is in the natural direction of the row entity or not. |
| [RowOffset](../RectangularOccurrencePattern/RectangularOccurrencePattern_RowOffset.md) | Property returning the Parameter object that controls the distance between rows. |
| [Suppressed](../RectangularOccurrencePattern/RectangularOccurrencePattern_Suppressed.md) | Returns the suppress state of the occurrence pattern. |
| [Type](../RectangularOccurrencePattern/RectangularOccurrencePattern_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../RectangularOccurrencePattern/RectangularOccurrencePattern_Visible.md) | Gets/Sets the Visible property for the pattern. |

## Accessed From

[OccurrencePatterns.AddRectangularPattern](../OccurrencePatterns/OccurrencePatterns_AddRectangularPattern.md), [RectangularOccurrencePatternProxy.NativeObject](../RectangularOccurrencePatternProxy/RectangularOccurrencePatternProxy_NativeObject.md)

## Derived Classes

[RectangularOccurrencePatternProxy](../RectangularOccurrencePatternProxy/RectangularOccurrencePatternProxy.md)

## Version

Introduced in version 6
