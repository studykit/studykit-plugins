# DerivedFuturePartDefinition Object

## Description

The DerivedFuturePartDefinition object is used to describe which entities within a future part will be used during the creation of the DerivedFuturePartComponent. It is also used when querying and editing an existing derived future part. When a DerivedFuturePartDefinition is initially created it is set so all available entities will be included in the derived part. Note: DerivedFuturePartDefinition object will become invalid after it has been set in the DerivedFuturePartComponent object i.e; all the properties will return failure.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ExcludeAll](../DerivedFuturePartDefinition/DerivedFuturePartDefinition_ExcludeAll.md) | Method that causes all entities within the derived part descriptor to be set to kDerivedExcludeAll. This method excludes all solids, surfaces, sketches, 3d sketches, sketch blocks, sketch block definitions, workfeatures, parameters and iMate definitions. |
| [IncludeAll](../DerivedFuturePartDefinition/DerivedFuturePartDefinition_IncludeAll.md) | Method that causes all entities within the derived part descriptor to be set to kDerivedIncludeAll. This method includes all solids, surfaces, sketches, 3d sketches, sketch blocks, sketch block definitions, workfeatures, parameters and iMate definitions. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveDesignViewRepresentation](../DerivedFuturePartDefinition/DerivedFuturePartDefinition_ActiveDesignViewRepresentation.md) | Read-write property that gets and sets the name of the active Design View Representation for the derived part. An empty string indicates the Master design view is used. The IsAssociativeDesignView property indicates if an associate link to the design view is created or not. |
| [Application](../DerivedFuturePartDefinition/DerivedFuturePartDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [FullFileName](../DerivedFuturePartDefinition/DerivedFuturePartDefinition_FullFileName.md) | Read-only property that gets the full filename of the derived document. |
| [IncludeAllSolids](../DerivedFuturePartDefinition/DerivedFuturePartDefinition_IncludeAllSolids.md) | Read-write property that defines whether all solids are included in the derived part. Valid input for this property is kDerivedIncludeAll, kDerivedExcludeAll, and kDerivedIndividualDefined. If set to kDerivedIncludeAll, all solids will be included. If set to kDerivedExcludeAll, no solids will be included. If set to kDerivedIndividualDefined, then the inclusion state of each solid is defined by the solid itself. The available solids are accessed using the Solids property of the DerivedPartDefinition object. |
| [IncludeAllSurfaces](../DerivedFuturePartDefinition/DerivedFuturePartDefinition_IncludeAllSurfaces.md) | Read-write property that defines whether all surfaces are included in the derived part. Valid input for this property is kDerivedIncludeAll, kDerivedExcludeAll, and kDerivedIndividualDefined. If set to kDerivedIncludeAll, all surfaces will be included. If set to kDerivedExcludeAll, no surfaces will be imported. If set to kDerivedIndividualDefined, then the inclusion state of each surface is defined by the surface itself. The available surfaces are accessed using the Surfaces property of the DerivedPartDefinition object. |
| [IsAssociativeDesignView](../DerivedFuturePartDefinition/DerivedFuturePartDefinition_IsAssociativeDesignView.md) | Read-write property that gets and sets if there is an associative link to the specified design view. When creating a new derived part, setting this property to True (which is the default) will create a derivation that is associative to the design view. This can only be set to True when a design view other than the master design view is specified. |
| [Solids](../DerivedFuturePartDefinition/DerivedFuturePartDefinition_Solids.md) | Read-only property that gets the collection of solids available in the selected part along with the inclusion option for each solid. |
| [Surfaces](../DerivedFuturePartDefinition/DerivedFuturePartDefinition_Surfaces.md) | Read-only property that gets the collection of surfaces available in the selected part along with the inclusion option for each surface. |
| [Type](../DerivedFuturePartDefinition/DerivedFuturePartDefinition_Type.md) | Read-only property returning kDerivedFuturePartDefinitionObject indicating the type of object. |

## Accessed From

[DerivedFuturePartComponent.Definition](../DerivedFuturePartComponent/DerivedFuturePartComponent_Definition.md), [DerivedFuturePartComponentProxy.Definition](../DerivedFuturePartComponentProxy/DerivedFuturePartComponentProxy_Definition.md)

## Version

Introduced in version 2018
