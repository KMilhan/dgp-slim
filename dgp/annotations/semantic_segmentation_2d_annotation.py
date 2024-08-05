# Copyright 2021 Toyota Research Institute.  All rights reserved.
import io
import os

import numpy as np

from dgp.annotations.base_annotation import Annotation
from dgp.annotations.ontology import SemanticSegmentationOntology
from dgp.utils.dataset_conversion import (
    generate_uid_from_semantic_segmentation_2d_annotation,
)


class SemanticSegmentation2DAnnotation(Annotation):
    """Container for semantic segmentation annotation.

    Parameters
    ----------
    ontology: SemanticSegmentationOntology
        Ontology for semantic segmentation tasks.

    segmentation_image: np.array
        Numpy uint8 array encoding segmentation labels.

    """

    def __init__(self, ontology, segmentation_image):
        super().__init__(ontology)
        assert isinstance(
            self._ontology, SemanticSegmentationOntology
        ), "Trying to load annotation with wrong type of ontology!"
        assert isinstance(segmentation_image, np.ndarray)
        assert segmentation_image.dtype == np.uint8
        assert len(segmentation_image.shape) == 2
        self._segmentation_image = segmentation_image


    def _convert_contiguous_to_class(self):
        """Helper function to run pre processing prior to saving.

        Returns
        -------
        segmentation_image: np.array
            A copy of self._segmentation_image with contiguous_id mapped back to class_id for saving

        """
        # Convert the segmentation image back to original class IDs
        reverse_label_lookup = (
            np.ones(self.ontology.VOID_ID + 1, dtype=np.uint8) * self.ontology.VOID_ID
        )
        for contiguous_id, class_id in self.ontology.contiguous_id_to_class_id.items():
            reverse_label_lookup[contiguous_id] = class_id

        # Create a copy and map IDs back to original set
        segmentation_image = np.copy(self._segmentation_image)
        not_ignore = segmentation_image != self.ontology.VOID_ID
        segmentation_image[not_ignore] = reverse_label_lookup[
            segmentation_image[not_ignore]
        ]
        return segmentation_image


    def render(self):
        """TODO: Rendering function for semantic segmentation images."""
        raise NotImplementedError

    @property
    def label(self):
        return self._segmentation_image

    @property
    def hexdigest(self):
        """Reproducible hash of annotation."""
        return generate_uid_from_semantic_segmentation_2d_annotation(
            self._segmentation_image
        )
