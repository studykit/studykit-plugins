# PresentationComponent Object

## Description

PresentationComponent Object.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Appearance](../PresentationComponent/PresentationComponent_Appearance.md) | Read-only property that gets and sets the current appearance for this presentation component. |
| [AppearanceSourceType](../PresentationComponent/PresentationComponent_AppearanceSourceType.md) | Read-only property that gets and sets the source of the appearance for this presentation component. This can be set to kMaterialAppearance to clear the override. |
| [Application](../PresentationComponent/PresentationComponent_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [IsLeaf](../PresentationComponent/PresentationComponent_IsLeaf.md) | Read-only property that returns whether this component is leaf component or not. |
| [MeshFeatureSets](../PresentationComponent/PresentationComponent_MeshFeatureSets.md) | Read-only property that returns all the PresentationMeshFeatureSet objects contained within the presentation component. |
| [Name](../PresentationComponent/PresentationComponent_Name.md) | Read-only property that returns the presentation component name. |
| [Opacity](../PresentationComponent/PresentationComponent_Opacity.md) | Read-only property that gets the opacity of this presentation component. |
| [Parent](../PresentationComponent/PresentationComponent_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [ParentComponent](../PresentationComponent/PresentationComponent_ParentComponent.md) | Read-only property that returns the parent PresentationComponent object. This property is only valid for the components in a multi-level assembly that are not in the top level. |
| [SubComponents](../PresentationComponent/PresentationComponent_SubComponents.md) | Read-only property that returns the collection of components for a PresentationComponent object. This property applies to components that represent a. |
| [SurfaceBodies](../PresentationComponent/PresentationComponent_SurfaceBodies.md) | Read-only property that returns all the PresentationBody objects contained within the presentation component. |
| [Transformation](../PresentationComponent/PresentationComponent_Transformation.md) | Read-only property that returns the Matrix object indicating the transform of the component. |
| [Type](../PresentationComponent/PresentationComponent_Type.md) | Gets the constant that indicates the type of this object. |
| [Visible](../PresentationComponent/PresentationComponent_Visible.md) | Read-only property that gets the visibility of the presentation component. |

## Accessed From

[PresentationBody.Parent](../PresentationBody/PresentationBody_Parent.md), [PresentationComponent.ParentComponent](../PresentationComponent/PresentationComponent_ParentComponent.md), [PresentationComponentsEnumerator.Item](../PresentationComponentsEnumerator/PresentationComponentsEnumerator_Item.md), [PresentationMeshFeatureSet.Parent](../PresentationMeshFeatureSet/PresentationMeshFeatureSet_Parent.md), [PresentationScene.TopSceneComponent](../PresentationScene/PresentationScene_TopSceneComponent.md), [PresentationTrail.PresentationComponent](../PresentationTrail/PresentationTrail_PresentationComponent.md)

## Version

Introduced in version 2018
