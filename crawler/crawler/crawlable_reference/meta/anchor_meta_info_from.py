from .bs_anchor_meta_info import BsAnchorMetaInfo


class AnchorMetaInfoFrom:
    @staticmethod
    def bs_anchor(bs_anchor):
        return BsAnchorMetaInfo(
            bs_parent=bs_anchor.bs.parent,
            bs_in=bs_anchor.bs
        )
