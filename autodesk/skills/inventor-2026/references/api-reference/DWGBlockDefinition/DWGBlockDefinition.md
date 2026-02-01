# DWGBlockDefinition Object

## Description

DWGBlockDefinition Object.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AcadSupportedProxies](../DWGBlockDefinition/DWGBlockDefinition_AcadSupportedProxies.md) | Read-only property that returns the DWGAcadSupportedProxiesEnumerator collection object. |
| [Application](../DWGBlockDefinition/DWGBlockDefinition_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Arcs](../DWGBlockDefinition/DWGBlockDefinition_Arcs.md) | Read-only property that returns the DWGArcsEnumerator collection object. |
| [BlockReferences](../DWGBlockDefinition/DWGBlockDefinition_BlockReferences.md) | Read-only property that returns the DWGBlockReferencesEnumerator collection object. |
| [EllipticalArcs](../DWGBlockDefinition/DWGBlockDefinition_EllipticalArcs.md) | Read-only property that returns the DWGEllipticalArcsEnumerator collection object. |
| [Entities](../DWGBlockDefinition/DWGBlockDefinition_Entities.md) | Read-only property that returns the DWGEntitiesEnumerator collection object. |
| [IsModelSpaceDefinition](../DWGBlockDefinition/DWGBlockDefinition_IsModelSpaceDefinition.md) | Read-only property that returns whether this DWGBlockDefinition is indicating the model space definition. |
| [Lines](../DWGBlockDefinition/DWGBlockDefinition_Lines.md) | Read-only property that returns the DWGLinesEnumerator collection object. |
| [Parent](../DWGBlockDefinition/DWGBlockDefinition_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Points](../DWGBlockDefinition/DWGBlockDefinition_Points.md) | Read-only property that returns the DWGPointsEnumerator collection object. |
| [Polylines](../DWGBlockDefinition/DWGBlockDefinition_Polylines.md) | Read-only property that returns the DWGPolylinesEnumerator collection object. |
| [Polylines2D](../DWGBlockDefinition/DWGBlockDefinition_Polylines2D.md) | Read-only property that returns the DWGPolylines2DEnumerator collection object. |
| [Polylines3D](../DWGBlockDefinition/DWGBlockDefinition_Polylines3D.md) | Read-only property that returns the DWGPolylines3DEnumerator collection object. |
| [Splines](../DWGBlockDefinition/DWGBlockDefinition_Splines.md) | Read-only property that returns the DWGSplinesEnumerator collection object. |
| [Type](../DWGBlockDefinition/DWGBlockDefinition_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[DWGBlockDefinitionProxy.NativeObject](../DWGBlockDefinitionProxy/DWGBlockDefinitionProxy_NativeObject.md), [DWGBlockReference.Definition](../DWGBlockReference/DWGBlockReference_Definition.md), [DWGBlockReferenceProxy.Definition](../DWGBlockReferenceProxy/DWGBlockReferenceProxy_Definition.md), [ImportedDWGComponent.ModelSpaceDefinition](../ImportedDWGComponent/ImportedDWGComponent_ModelSpaceDefinition.md), [ImportedDWGComponentProxy.ModelSpaceDefinition](../ImportedDWGComponentProxy/ImportedDWGComponentProxy_ModelSpaceDefinition.md)

## Derived Classes

[DWGBlockDefinitionProxy](../DWGBlockDefinitionProxy/DWGBlockDefinitionProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [ImportedDWGComponent Creation](../../sample-programs/ImportedDWGComponentCreation_Sample.md) | This sample demonstrates how to create an imported DWG component into Inventor part document, and project the DWG entities onto Inventor planar sketch. |

## Version

Introduced in version 2016
