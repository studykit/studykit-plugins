# FeatureBasedOccurrencePattern Object

Derived from: [OccurrencePattern](../OccurrencePattern/OccurrencePattern.md) Object

## Description

The FeatureBasedOccurrencePattern object represents a feature-based occurrence pattern.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../FeatureBasedOccurrencePattern/FeatureBasedOccurrencePattern_Delete.md) | Method that deletes the pattern. |
| [GetReferenceKey](../FeatureBasedOccurrencePattern/FeatureBasedOccurrencePattern_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [Suppress](../FeatureBasedOccurrencePattern/FeatureBasedOccurrencePattern_Suppress.md) | Suppress the occurrence pattern. |
| [Unsuppress](../FeatureBasedOccurrencePattern/FeatureBasedOccurrencePattern_Unsuppress.md) | Unsuppress the occurrence pattern. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FeatureBasedOccurrencePattern/FeatureBasedOccurrencePattern_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../FeatureBasedOccurrencePattern/FeatureBasedOccurrencePattern_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [FeaturePattern](../FeatureBasedOccurrencePattern/FeatureBasedOccurrencePattern_FeaturePattern.md) | Gets/Sets the feature pattern used as input for this occurrence pattern. |
| [HealthStatus](../FeatureBasedOccurrencePattern/FeatureBasedOccurrencePattern_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsPatternElement](../FeatureBasedOccurrencePattern/FeatureBasedOccurrencePattern_IsPatternElement.md) | Property that indicates whether this occurrence pattern is itself an element of a parent pattern. In the case where this occurrence pattern represents a pattern element, this property returns True. The PatternElement property can be used to get that pattern element. |
| [Name](../FeatureBasedOccurrencePattern/FeatureBasedOccurrencePattern_Name.md) | Gets/Sets the name for the pattern. |
| [OccurrencePatternElements](../FeatureBasedOccurrencePattern/FeatureBasedOccurrencePattern_OccurrencePatternElements.md) | Property returning an OccurrencePatternElements collection object. The first element within this collection will contain the components that were provided as input for the pattern. |
| [Parent](../FeatureBasedOccurrencePattern/FeatureBasedOccurrencePattern_Parent.md) | Property that returns the parent of the object. |
| [ParentComponents](../FeatureBasedOccurrencePattern/FeatureBasedOccurrencePattern_ParentComponents.md) | Property that gets and sets the components used as input for the pattern. |
| [PatternElement](../FeatureBasedOccurrencePattern/FeatureBasedOccurrencePattern_PatternElement.md) | Property that returns the pattern element this occurrence pattern represents. In the case where this occurrence pattern is not part of a parent pattern this property returns Nothing. The IsPatternElement property can be used to check if this occurrence pattern is part of a parent pattern. |
| [Suppressed](../FeatureBasedOccurrencePattern/FeatureBasedOccurrencePattern_Suppressed.md) | Returns the suppress state of the occurrence pattern. |
| [Type](../FeatureBasedOccurrencePattern/FeatureBasedOccurrencePattern_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../FeatureBasedOccurrencePattern/FeatureBasedOccurrencePattern_Visible.md) | Gets/Sets the Visible property for the pattern. |

## Accessed From

[FeatureBasedOccurrencePatternProxy.NativeObject](../FeatureBasedOccurrencePatternProxy/FeatureBasedOccurrencePatternProxy_NativeObject.md), [OccurrencePatterns.AddFeatureBasedPattern](../OccurrencePatterns/OccurrencePatterns_AddFeatureBasedPattern.md)

## Derived Classes

[FeatureBasedOccurrencePatternProxy](../FeatureBasedOccurrencePatternProxy/FeatureBasedOccurrencePatternProxy.md)

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |