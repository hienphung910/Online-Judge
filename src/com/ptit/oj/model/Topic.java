package com.ptit.oj.model;

/**
 * Mot chu de trong lo trinh hoc, vi du "Vong lap" hay "Xau ky tu".
 *
 * Thu tu hoc (order) chinh la thu tu dong trong data/topics.txt, nen giao vien
 * doi lo trinh chi can doi cho cac dong - khong phai sua tung bai tap.
 * Bai tap tro toi chu de bang ma (Problem.getTopic()), khong giu tham chieu
 * truc tiep, de bai cu tro toi chu de da bi xoa van nap duoc binh thuong.
 */
public class Topic extends Entity {

    private final String name;
    private final String description;
    private final int order;

    public Topic(String id, String name, String description, int order) {
        super(id);
        this.name = name;
        this.description = description == null ? "" : description;
        this.order = order;
    }

    public String getName() { return name; }
    public String getDescription() { return description; }
    /** Vi tri trong lo trinh, tinh tu 1. */
    public int getOrder() { return order; }

    @Override
    public String describe() {
        return order + ". " + name + (description.isEmpty() ? "" : " - " + description);
    }
}
