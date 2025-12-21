# CircularOccurrencePattern Object

Derived from: [OccurrencePattern](../OccurrencePattern/OccurrencePattern.md) Object

## Description

The CircularOccurrencePattern object represents a circular pattern of assembly occurrences.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../CircularOccurrencePattern/CircularOccurrencePattern_Delete.md) | Method that deletes the pattern. |
| [GetReferenceKey](../CircularOccurrencePattern/CircularOccurrencePattern_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [Suppress](../CircularOccurrencePattern/CircularOccurrencePattern_Suppress.md) | Suppress the occurrence pattern. |
| [Unsuppress](../CircularOccurrencePattern/CircularOccurrencePattern_Unsuppress.md) | Unsuppress the occurrence pattern. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AngleOffset](../CircularOccurrencePattern/CircularOccurrencePattern_AngleOffset.md) | Property returning the Parameter object that controls the angle offset between pattern instances. |
| [Application](../CircularOccurrencePattern/CircularOccurrencePattern_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../CircularOccurrencePattern/CircularOccurrencePattern_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [AxisEntity](../CircularOccurrencePattern/CircularOccurrencePattern_AxisEntity.md) | Gets/Sets the entity used to define the axis of the pattern. |
| [AxisEntityNaturalDirection](../CircularOccurrencePattern/CircularOccurrencePattern_AxisEntityNaturalDirection.md) | Gets/Sets whether the axis direction is in the natural direction of the axis entity or not. |
| [ElementCount](../CircularOccurrencePattern/CircularOccurrencePattern_ElementCount.md) | Property returning the Parameter object that controls the number of elements in the pattern. |
| [HealthStatus](../CircularOccurrencePattern/CircularOccurrencePattern_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsPatternElement](../CircularOccurrencePattern/CircularOccurrencePattern_IsPatternElement.md) | Property that indicates whether this occurrence pattern is itself an element of a parent pattern. In the case where this occurrence pattern represents a pattern element, this property returns True. The PatternElement property can be used to get that pattern element. |
| [LockRotation](../CircularOccurrencePattern/CircularOccurrencePattern_LockRotation.md) | Read-write property that gets and sets whether the patterned elements keep the same rotation as their parent occurrences. This defaults to False when the CircularOccurrencePattern is just created indicates that the patterned elements will be rotated. |
| [Name](../CircularOccurrencePattern/CircularOccurrencePattern_Name.md) | Gets/Sets the name for the pattern. |
| [OccurrencePatternElements](../CircularOccurrencePattern/CircularOccurrencePattern_OccurrencePatternElements.md) | Property returning an OccurrencePatternElements collection object. The first element within this collection will contain the components that were provided as input for the pattern. |
| [Parent](../CircularOccurrencePattern/CircularOccurrencePattern_Parent.md) | Property that returns the parent of the object. |
| [ParentComponents](../CircularOccurrencePattern/CircularOccurrencePattern_ParentComponents.md) | Property that gets and sets the components used as input for the pattern. |
| [PatternElement](../CircularOccurrencePattern/CircularOccurrencePattern_PatternElement.md) | Property that returns the pattern element this occurrence pattern represents. In the case where this occurrence pattern is not part of a parent pattern this property returns Nothing. The IsPatternElement property can be used to check if this occurrence pattern is part of a parent pattern. |
| [PatternRadiusPoint](../CircularOccurrencePattern/CircularOccurrencePattern_PatternRadiusPoint.md) | Read-write property that gets and sets the point used to define the pattern radius against the rotation axis. This property returns Nothing when the LockRotation is False. When the LockRotation is set to True, this property returns a Point object indicating th. |
| [PositioningMethod](../CircularOccurrencePattern/CircularOccurrencePattern_PositioningMethod.md) | Read-write property that gets and sets the enum indicating the positioning method used for the component pattern. |
| [Suppressed](../CircularOccurrencePattern/CircularOccurrencePattern_Suppressed.md) | Returns the suppress state of the occurrence pattern. |
| [Type](../CircularOccurrencePattern/CircularOccurrencePattern_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../CircularOccurrencePattern/CircularOccurrencePattern_Visible.md) | Gets/Sets the Visible property for the pattern. |

## Accessed From

[CircularOccurrencePatternProxy.NativeObject](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_NativeObject.md), [OccurrencePatterns.AddCircularPattern](../OccurrencePatterns/OccurrencePatterns_AddCircularPattern.md)

## Derived Classes

[CircularOccurrencePatternProxy](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy.md)

## Version

Introduced in version 6
